#!/usr/bin/env python3
"""
OpenClaw Agent Mode Self-Check Tool

Ask yourself: Am I Captain, Architect, or Abdicator right now?

Usage:
    python agent-check.py
    python agent-check.py --mode captain
    python agent-check.py --tips
"""

import argparse
import sys
from datetime import datetime

MODES = {
    "captain": {
        "name": "将才 (Captain)",
        "emoji": "⚔️",
        "description": "Works alongside agent, learns while delegating",
        "outcome": "Growth ↑",
        "checklist": [
            "I'm working alongside the agent",
            "I'm observing *how* it solves problems",
            "I'm learning from each delegation",
            "I understand the solution enough to explain it"
        ]
    },
    "architect": {
        "name": "帅才 (Architect)",
        "emoji": "🏛️",
        "description": "Designs systems, probes boundaries, verifies quality",
        "outcome": "Efficiency ↑",
        "checklist": [
            "I've probed the agent's capability boundaries",
            "I've decomposed the goal into reliable units",
            "I've set up verification checkpoints",
            "I own the outcome, not just the delegation"
        ]
    },
    "abdicator": {
        "name": "刘禅 (Abdicator)",
        "emoji": "⚠️",
        "description": "Throws tasks at agent, accepts whatever comes back",
        "outcome": "Decline ↓",
        "checklist": [
            "I threw a task and accepted whatever came back",
            "I didn't check the quality",
            "I don't understand how the solution works",
            "I can't explain what the agent did"
        ]
    }
}

def print_banner():
    print("=" * 50)
    print("🤖 OpenClaw Agent Mode Self-Check")
    print("=" * 50)
    print()

def check_mode(mode_key):
    """Interactive checklist for a specific mode"""
    mode = MODES[mode_key]
    print(f"\n{mode['emoji']} {mode['name']}")
    print(f"   {mode['description']}")
    print(f"   Outcome: {mode['outcome']}")
    print()
    print("Checklist:")
    
    score = 0
    for i, item in enumerate(mode['checklist'], 1):
        response = input(f"  [{i}] {item}? (y/n): ").lower().strip()
        if response == 'y':
            score += 1
    
    print()
    print(f"Score: {score}/{len(mode['checklist'])}")
    
    if mode_key == "abdicator":
        if score >= 2:
            print("⚠️  WARNING: You're in Abdicator mode!")
            print("   Consider switching to Captain or Architect mode.")
        else:
            print("✅ Good! You're not in Abdicator mode.")
    else:
        if score >= 3:
            print(f"✅ You're effectively using {mode['name']} mode!")
        else:
            print(f"💡 Tips to improve your {mode['name']} mode:")
            print("   - Pay more attention to how AI solves problems")
            print("   - Verify outputs at key checkpoints")

def interactive_check():
    """Interactive mode detection"""
    print_banner()
    print("Answer these questions to detect your current mode:\n")
    
    print("1. Did you delegate a task to AI?")
    response1 = input("   (y/n): ").lower().strip()
    
    if response1 != 'y':
        print("\n📝 You're not using AI agents yet.")
        print("   Start by delegating a simple task and observe.")
        return
    
    print("\n2. Do you understand how AI solved it?")
    response2 = input("   (y/n): ").lower().strip()
    
    if response2 != 'y':
        print("\n" + "=" * 50)
        print("⚠️  You're in ABDICATOR mode!")
        print("=" * 50)
        print("\nYou're being used by AI, not using AI.")
        print("\nTo switch to Captain mode:")
        print("  1. Go back and understand what AI did")
        print("  2. Ask AI to explain its approach")
        print("  3. Learn from each delegation")
        return
    
    print("\n3. Did you learn something new from this?")
    response3 = input("   (y/n): ").lower().strip()
    
    print("\n" + "=" * 50)
    if response3 == 'y':
        print("⚔️  You're in CAPTAIN mode!")
        print("=" * 50)
        print("\nYou're growing! Keep learning from each interaction.")
    else:
        print("🏛️  You're in ARCHITECT mode!")
        print("=" * 50)
        print("\nYou're efficient! Make sure to verify at key checkpoints.")

def show_tips():
    """Show tips for each mode"""
    print_banner()
    print("💡 Tips for each mode:\n")
    
    print("⚔️  CAPTAIN MODE (Growth)")
    print("   - Watch HOW AI solves problems, not just the output")
    print("   - Ask AI to explain its reasoning")
    print("   - Try to replicate the solution yourself")
    print("   - Every delegation is a learning opportunity")
    print()
    
    print("🏛️  ARCHITECT MODE (Efficiency)")
    print("   - Test AI's boundaries before delegating")
    print("   - Break complex goals into smaller units")
    print("   - Set up verification checkpoints")
    print("   - Own the outcome, not just the task")
    print()
    
    print("⚠️  ABDICATOR MODE (Avoid!)")
    print("   - If you can't explain what AI did → Abdicator")
    print("   - If you didn't verify quality → Abdicator")
    print("   - Fix: Go back, understand, learn")
    print()

def main():
    parser = argparse.ArgumentParser(
        description="OpenClaw Agent Mode Self-Check Tool"
    )
    parser.add_argument(
        "--mode", "-m",
        choices=["captain", "architect", "abdicator"],
        help="Check a specific mode"
    )
    parser.add_argument(
        "--tips", "-t",
        action="store_true",
        help="Show tips for each mode"
    )
    
    args = parser.parse_args()
    
    if args.tips:
        show_tips()
    elif args.mode:
        print_banner()
        check_mode(args.mode)
    else:
        interactive_check()

if __name__ == "__main__":
    main()
