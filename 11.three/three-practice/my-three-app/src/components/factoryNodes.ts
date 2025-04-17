export type Node = {
    id: string;
    type: 'pickup' | 'finished' | 'line_input' | 'line_output' | 'charge' | 'wait';
    position: [number, number, number];
  };
  
  export const factoryNodes: Node[] = [];

// 자재창고 입구 15개
for (let i = 0; i < 15; i++) {
  factoryNodes.push({
    id: `PICKUP_${i + 1}`,
    type: 'pickup',
    position: [-15 + i * 2, 0, -10],
  });
}

// 완제품창고 입구 5개
for (let i = 0; i < 5; i++) {
  factoryNodes.push({
    id: `FINISHED_${i + 1}`,
    type: 'finished',
    position: [10 + i * 2, 0, -10],
  });
}

// 생산라인 20개 (투입/배출)
for (let i = 0; i < 20; i++) {
  factoryNodes.push({
    id: `LINE_${i + 1}_INPUT`,
    type: 'line_input',
    position: [-10 + (i % 10) * 2, 0, 0],
  });
  factoryNodes.push({
    id: `LINE_${i + 1}_OUTPUT`,
    type: 'line_output',
    position: [-10 + (i % 10) * 2, 0, 5],
  });
}

// 충전노드 3개
for (let i = 0; i < 3; i++) {
  factoryNodes.push({
    id: `CHARGE_${i + 1}`,
    type: 'charge',
    position: [-5 + i * 5, 0, 10],
  });
}

// 대기노드 30개 (6열 x 5행)
for (let i = 0; i < 30; i++) {
  factoryNodes.push({
    id: `WAIT_${i + 1}`,
    type: 'wait',
    position: [-15 + (i % 6) * 5, 0, 15 + Math.floor(i / 6) * 3],
  });
}
