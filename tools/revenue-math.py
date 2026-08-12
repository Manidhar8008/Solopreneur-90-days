#!/usr/bin/env python3
"""Simple revenue-model calculator for Solopreneur 90 Days."""

import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target", type=float, required=True, help="Annual revenue target")
    p.add_argument("--price", type=float, required=True, help="Average annual revenue per customer")
    p.add_argument("--close-rate", type=float, default=0.20, help="Sales close rate, e.g. 0.20")
    args = p.parse_args()

    customers = args.target / args.price
    opportunities = customers / args.close_rate

    print(f"Target annual revenue: ${args.target:,.0f}")
    print(f"Average annual revenue/customer: ${args.price:,.0f}")
    print(f"Customers required: {customers:,.1f}")
    print(f"Qualified opportunities at {args.close_rate:.0%} close rate: {opportunities:,.1f}")

if __name__ == "__main__":
    main()
