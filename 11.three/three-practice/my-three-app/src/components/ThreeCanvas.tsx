import { useEffect, useRef } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { createAMRRobot } from './AMRRobot';
import { factoryNodes } from './factoryNodes'; // 경로 맞춰서 import

type AMRState = {
    group: THREE.Group;
    route: string[]; // 노드 ID 배열
    currentTargetIndex: number;
  };  

const ThreeCanvas = () => {
  // Three.js에서 렌더링된 DOM 요소를 붙일 div를 참조
  const mountRef = useRef<HTMLDivElement>(null);
  
  const nodeColorMap: Record<Node['type'], string> = {
    pickup: '#1976d2',
    finished: '#388e3c',
    line_input: '#fbc02d',
    line_output: '#ff7043',
    charge: '#ab47bc',
    wait: '#90a4ae',
  };
  const amrStatesRef = useRef<AMRState[]>([]);



  useEffect(() => {
    // 장면 생성
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xe0e0e0); // 너무 검은 배경은 착시 유발

    // 카메라 설정 (시야각, 화면 비율, near, far)
    const camera = new THREE.PerspectiveCamera(
      75, 
      window.innerWidth / window.innerHeight, 
      0.1, 
      1000
    );
    camera.position.set(5, 5, 5); // 약간 위에서 보는 느낌
    camera.lookAt(0, 0.5, 0); // 큐브 중심 바라보기

    // 렌더러 생성 및 사이즈 설정
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);

    // renderer의 canvas 요소를 mountRef가 가리키는 DOM에 추가
    mountRef.current?.appendChild(renderer.domElement);

    // 🎮 OrbitControls 생성 (카메라 & renderer.domElement 전달)
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true; // 부드러운 감속 효과
    controls.dampingFactor = 0.05; // 감속 정도
    controls.enableZoom = true; // 줌 허용
    // controls.enablePan = true; // 패닝(이동) 허용
    controls.target.set(0, 0, 0); // 큐브 중심을 타겟으로 고정
    controls.update();

    // 바닥 및 조명
    scene.add(new THREE.GridHelper(10, 10));
    scene.add(new THREE.AxesHelper(5));
    scene.add(new THREE.AmbientLight(0xffffff, 0.4));
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(5, 5, 5);
    scene.add(light);

    // 박스(큐브) 형상과 재질을 생성하고 장면에 추가
    // const geometry = new THREE.BoxGeometry(); // 정육면체 형상
    // const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // 녹색 재질
    // const cube = new THREE.Mesh(geometry, material); // 형상 + 재질 = 메시(입체 객체)
    // cube.position.y = 0.5; // 바닥 위에 정확히 놓이도록 위치 조정
    // scene.add(cube);

    // Grid (바닥)
    const gridHelper = new THREE.GridHelper(80, 80);
    scene.add(gridHelper);

    // Axes Helper (X: 빨, Y: 초록, Z: 파)
    const axesHelper = new THREE.AxesHelper(5);
    scene.add(axesHelper);

    // Render once (회전 없으므로 애니메이션 루프 불필요)
    // renderer.render(scene, camera);

    // 여러 개 로봇을 만들고 싶다면 이런 식으로 위치 리스트
    // const robotPositions: [number, number, number][] = [
    //     [0, 0, 0],
    //     // [2, 0, 1],
    //     // [-2, 0, -1],
    // ];

    const getRandomRoute = (): string[] => {
        const from = factoryNodes[Math.floor(Math.random() * factoryNodes.length)].id;
        let to = from;
        while (to === from) {
          to = factoryNodes[Math.floor(Math.random() * factoryNodes.length)].id;
        }
        return [from, to];
      };

    factoryNodes.forEach((node) => {
        const color = nodeColorMap[node.type]; // ✅ 타입별 색상 선택

        const sphere = new THREE.Mesh(
          new THREE.SphereGeometry(0.3, 16, 16),
          new THREE.MeshStandardMaterial({ color })
        );
        sphere.position.set(...node.position);
        scene.add(sphere);
      });

    // 4행 x 5열 격자 형태로 배치 (1.5m 간격)
    const robotPositions: [number, number, number][] = [];

    for (let i = 0; i < 20; i++) {
    const x = -6 + (i % 5) * 3; // x: -6, -3, 0, 3, 6
    const z = -6 + Math.floor(i / 5) * 3; // z: -6, -3, 0, 3
    robotPositions.push([x, 0, z]);
    }

    // 로봇 생성
    robotPositions.forEach((pos) => {
        const amrGroup = createAMRRobot(scene, pos);  // ✅ group 반환 받기
        const route = getRandomRoute(); // 아래에서 정의할 함수
        amrStatesRef.current.push({
            group: amrGroup,
            route,
            currentTargetIndex: 0,
          });    });

    let direction = 1; // ➡️ 오른쪽으로 시작

    // 👇 animate 함수 추가
    const animate = () => {
        requestAnimationFrame(animate);
        controls.update();
      
        const speed = 0.02;
      
        amrStatesRef.current.forEach((amrState) => {
          const { group, route, currentTargetIndex } = amrState;
      
          if (!route[currentTargetIndex]) return;
      
          const targetNode = factoryNodes.find((n) => n.id === route[currentTargetIndex]);
          if (!targetNode) return;
      
          const [tx, , tz] = targetNode.position;
          const direction = new THREE.Vector3(tx - group.position.x, 0, tz - group.position.z);
          const distance = direction.length();
      
          if (distance < 0.1) {
            // 도착하면 다음 경로로
            amrState.currentTargetIndex++;
            if (amrState.currentTargetIndex >= amrState.route.length) {
              const newRoute = getRandomRoute(); // 새 경로 재할당
              amrState.route = newRoute;
              amrState.currentTargetIndex = 0;
            }
          } else {
            direction.normalize();
            group.position.x += direction.x * speed;
            group.position.z += direction.z * speed;
          }
        });
      
        renderer.render(scene, camera);
      };
      
    animate(); // 실행
  

    // 컴포넌트 언마운트 시 정리
    return () => {
      controls.dispose(); // 컨트롤 해제
      renderer.dispose(); // 렌더러 메모리 해제
      mountRef.current?.removeChild(renderer.domElement); // DOM 정리
    };
  }, []); // 한 번만 실행

  // 📦 9. Three.js 캔버스를 붙일 div 반환
  return <div ref={mountRef} />;
};

export default ThreeCanvas;
