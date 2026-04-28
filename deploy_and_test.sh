#!/bin/bash
set -e

echo ""
echo "============================================"
echo "   Playwright Deploy & Test Pipeline"
echo "============================================"

echo ""
echo "[1/3] Ensuring VM is up..."
vagrant up

echo ""
echo "[2/3] Installing dependencies..."
vagrant ssh -c "cd ~/app && pip3 install -r requirements.txt --quiet"

echo ""
echo "[3/3] Running Playwright tests..."
vagrant ssh -c "cd ~/app && pytest tests/e2e/ -v --junitxml=test-results.xml"

echo ""
echo "============================================"
echo "   Pipeline Complete"
echo "============================================"