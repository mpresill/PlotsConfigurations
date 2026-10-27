#!/usr/bin/env python3
"""
Build a table of EFT template weights from a MadGraph reweighting card.

Input : the reweight card (.dat). Only the comment lines in front of each block are used,
        for example "# cHWB=1, cHbox=1 rwgt_25" and "# SM rwgt_1".
Output: a JSON file and a CSV file. Each entry says which LHEReweightingWeight indices
        to combine, and with which coefficients, to get one template weight.

Entries written:
    sm
    sm_lin_quad_<op>            = w(op=+1)
    quad_<op>                   = 0.5*(w(op=+1) + w(op=-1)) - w(SM)
    sm_lin_quad_mixed_<a>_<b>   = w(a=+1, b=+1)

Index rule: block rwgt_N is LHEReweightingWeight[N-1]  (rwgt_1 = SM = index 0).

Usage:
    python make_weight_table.py CARD.dat [-o OUTPUT_PREFIX]
"""
import argparse
import csv
import json
import re
import sys
from itertools import combinations

COMMENT_RE = re.compile(r"^#\s*(?P<what>.+?)\s+rwgt_(?P<n>\d+)\s*$")


def parse_card(path):
    """Return ({N: {op: value}}, number_of_launch_lines). SM maps to an empty dict."""
    blocks = {}
    n_launch = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("launch"):
                n_launch += 1
                continue
            m = COMMENT_RE.match(line)
            if not m:
                continue
            n = int(m.group("n"))
            what = m.group("what")
            if n in blocks:
                sys.exit(f"ERROR: rwgt_{n} appears twice in the card.")
            if what.strip().upper() == "SM":
                blocks[n] = {}
                continue
            ops = {}
            for part in what.split(","):
                name, _, value = part.strip().partition("=")
                if not value:
                    sys.exit(f"ERROR: cannot read '{part}' in comment for rwgt_{n}.")
                ops[name.strip()] = float(value)
            blocks[n] = ops
    return blocks, n_launch


def check_blocks(blocks, n_launch):
    n_max = max(blocks)
    if sorted(blocks) != list(range(1, n_max + 1)):
        sys.exit("ERROR: the rwgt numbers are not 1..N without gaps.")
    if n_launch != len(blocks):
        sys.exit(f"ERROR: {n_launch} 'launch' lines but {len(blocks)} comment blocks.")
    if blocks[1] != {}:
        sys.exit("ERROR: rwgt_1 is not the SM block.")


def find_index(blocks, target):
    """Index (N-1) of the block whose non-zero coefficients equal `target` exactly."""
    hits = [n for n, ops in blocks.items() if ops == target]
    if len(hits) != 1:
        sys.exit(f"ERROR: expected exactly one block for {target}, found {len(hits)}.")
    return hits[0] - 1


def expression(terms):
    out = ""
    for t in terms:
        c, i = t["coefficient"], t["index"]
        w = f"LHEReweightingWeight[{i}]"
        mag = abs(c)
        piece = w if mag == 1 else f"{mag:g}*{w}"
        out += (" - " if c < 0 else (" + " if out else "")) + piece
    return out


def build_entries(blocks):
    sm = find_index(blocks, {})
    entries = [{
        "name": "sm", "kind": "sm", "operators": [],
        "terms": [{"index": sm, "coefficient": 1.0}],
    }]

    # Operators that have both a +1 and a -1 block, in card order.
    ops = []
    for n in sorted(blocks):
        for op in blocks[n]:
            if len(blocks[n]) == 1 and op not in ops:
                ops.append(op)

    for op in ops:
        plus = find_index(blocks, {op: 1.0})
        minus = find_index(blocks, {op: -1.0})
        entries.append({
            "name": f"sm_lin_quad_{op}", "kind": "sm_lin_quad", "operators": [op],
            "terms": [{"index": plus, "coefficient": 1.0}],
        })
        entries.append({
            "name": f"quad_{op}", "kind": "quad", "operators": [op],
            "terms": [{"index": plus, "coefficient": 0.5},
                      {"index": minus, "coefficient": 0.5},
                      {"index": sm, "coefficient": -1.0}],
        })

    # Pairs: use the operator order written in the card comment.
    for a, b in combinations(ops, 2):
        hits = [n for n, o in blocks.items() if o == {a: 1.0, b: 1.0}]
        if len(hits) != 1:
            sys.exit(f"ERROR: expected one block for the pair {a}, {b}, found {len(hits)}.")
        order = list(blocks[hits[0]].keys())
        entries.append({
            "name": f"sm_lin_quad_mixed_{order[0]}_{order[1]}",
            "alias": f"sm_lin_quad_mixed_{order[1]}_{order[0]}",
            "kind": "sm_lin_quad_mixed", "operators": order,
            "terms": [{"index": hits[0] - 1, "coefficient": 1.0}],
        })

    for e in entries:
        e["expression"] = expression(e["terms"])
    return entries


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("card")
    ap.add_argument("-o", "--output-prefix", default="eft_weights")
    args = ap.parse_args()

    blocks, n_launch = parse_card(args.card)
    check_blocks(blocks, n_launch)
    entries = build_entries(blocks)

    meta = {
        "source_card": args.card,
        "n_weights_in_card": len(blocks),
        "index_rule": "block rwgt_N is LHEReweightingWeight[N-1]; rwgt_1 (SM) is index 0",
        "note": ("Reweighting weights are normally ratios to the nominal weight. "
                 "Event weight = generator weight * expression."),
        "n_entries": len(entries),
    }
    with open(args.output_prefix + ".json", "w") as f:
        json.dump({"meta": meta, "entries": entries}, f, indent=2)
    with open(args.output_prefix + ".csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "expression"])
        for e in entries:
            w.writerow([e["name"], e["expression"]])

    print(f"{len(blocks)} blocks read, {len(entries)} entries written to "
          f"{args.output_prefix}.json and {args.output_prefix}.csv")


if __name__ == "__main__":
    main()
