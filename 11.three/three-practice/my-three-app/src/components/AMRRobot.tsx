import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three-stdlib';

export function createAMRRobot(scene: THREE.Scene, position: [number, number, number]) {
  const group = new THREE.Group();

  // 하단 본체
  const base = new THREE.Mesh(
    new RoundedBoxGeometry(1, 0.3, 1, 6, 0.08),
    new THREE.MeshStandardMaterial({ color: 0x444444 })
  );
  base.position.y = 0.15;
  group.add(base);

  // 상단 지지대 (롤러 위 받침)
  const support = new THREE.Mesh(
    new THREE.BoxGeometry(1, 0.05, 1),
    new THREE.MeshStandardMaterial({ color: 0x888888 })
  );
  support.position.y = 0.35;
  group.add(support);

  // 롤러 생성 (CylinderGeometry 회전축을 Z방향으로)
  const rollerMaterial = new THREE.MeshStandardMaterial({ color: 0xbbbbbb });
  const rollerGroup = new THREE.Group();

  const rollerCount = 8;
  for (let i = 0; i < rollerCount; i++) {
    const roller = new THREE.Mesh(
      new THREE.CylinderGeometry(0.06, 0.06, 1.0, 16), // 두께: 0.06 / 길이: 0.9
      rollerMaterial
    );
    roller.rotation.z = Math.PI / 2; // Z축으로 눕히기
    roller.position.set(
      0,
      0.36,
      -0.45 + (i / (rollerCount - 1)) * 0.9
    );
    rollerGroup.add(roller);
  }
  group.add(rollerGroup);

  // ✅ 여기에 추가!
  const wallMaterial = new THREE.MeshStandardMaterial({ color: 0x666666 });
  const wallGeometry = new THREE.BoxGeometry(0.02, 0.15, 1.0); // 얇고 높은 벽

  const leftWall = new THREE.Mesh(wallGeometry, wallMaterial);
  leftWall.position.set(-0.50, 0.43, 0); // 왼쪽 롤러 바깥에 맞게 조정
  group.add(leftWall);
  
  const rightWall = new THREE.Mesh(wallGeometry, wallMaterial);
  rightWall.position.set(0.50, 0.43, 0); // 오른쪽 롤러 바깥에 맞게 조정
  group.add(rightWall);
  
  // 위치 설정
  group.position.set(...position);
  scene.add(group);

  // 🔁 애니메이션 등록용으로 rollerGroup 반환.
  return group; // ✅ 전체 그룹 반환 
}
