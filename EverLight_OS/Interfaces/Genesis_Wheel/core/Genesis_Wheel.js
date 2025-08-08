/*
 * Genesis_Wheel.js
 *
 * This module draws a 12‑node morphogenetic wheel using native SVG API. The
 * wheel consists of a central node labeled "YOU" and twelve outer nodes
 * labeled D1 through D12. Each outer node is connected to the center by a
 * straight line. The drawing executes once on DOMContentLoaded but can be
 * re‑invoked to redraw the wheel if necessary.
 */

export function drawWheel() {
  const svg = document.getElementById('genesis-wheel');
  if (!svg) return;

  const centerX = svg.getAttribute('width') / 2;
  const centerY = svg.getAttribute('height') / 2;
  const radius = Math.min(centerX, centerY) * 0.75;

  // Remove any previous elements to avoid duplication on redraw.
  while (svg.firstChild) {
    svg.removeChild(svg.firstChild);
  }

  // Draw center node.
  const centerCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  centerCircle.setAttribute('cx', centerX);
  centerCircle.setAttribute('cy', centerY);
  centerCircle.setAttribute('r', 20);
  centerCircle.classList.add('node');
  svg.appendChild(centerCircle);

  // Label for the center node.
  const centerText = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  centerText.setAttribute('x', centerX);
  centerText.setAttribute('y', centerY + 5);
  centerText.setAttribute('text-anchor', 'middle');
  centerText.classList.add('node-label');
  centerText.textContent = 'YOU';
  svg.appendChild(centerText);

  // Draw outer nodes and connecting lines.
  for (let i = 0; i < 12; i++) {
    const angle = (i / 12) * Math.PI * 2;
    const x = centerX + radius * Math.cos(angle);
    const y = centerY + radius * Math.sin(angle);

    // Line from center to outer node.
    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', centerX);
    line.setAttribute('y1', centerY);
    line.setAttribute('x2', x);
    line.setAttribute('y2', y);
    line.classList.add('edge');
    svg.appendChild(line);

    // Outer node circle.
    const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    circle.setAttribute('cx', x);
    circle.setAttribute('cy', y);
    circle.setAttribute('r', 15);
    circle.classList.add('node');
    svg.appendChild(circle);

    // Label for the outer node.
    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    text.setAttribute('x', x);
    text.setAttribute('y', y + 5);
    text.setAttribute('text-anchor', 'middle');
    text.classList.add('node-label');
    text.textContent = `D${i + 1}`;
    svg.appendChild(text);
  }
}

// Automatically draw the wheel once the DOM is ready.
document.addEventListener('DOMContentLoaded', drawWheel);