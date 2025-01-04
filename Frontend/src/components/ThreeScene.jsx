import React, { useRef, useEffect } from "react";
import * as THREE from "three";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

function ThreeScene() {
  const mountRef = useRef(null);

  useEffect(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000,
    );
    const renderer = new THREE.WebGLRenderer({ alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    mountRef.current.appendChild(renderer.domElement);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(5, 10, 7.5);
    scene.add(directionalLight);

    const loader = new GLTFLoader();
    let handBones = {};
    loader.load(
      "/RiggedHand.glb",
      (gltf) => {
        const model = gltf.scene;
        scene.add(model);

        const box = new THREE.Box3().setFromObject(model);
        const center = new THREE.Vector3();
        box.getCenter(center);
        model.position.sub(center);

        const boneNames = [
          "0-1",
          "1-2",
          "2-3",
          "3-4",
          "0-5",
          "5-6",
          "6-7",
          "7-8",
          "5-9",
          "9-10",
          "10-11",
          "11-12",
          "0-17",
          "17-13",
          "13-14",
          "14-15",
          "15-16",
          "17-18",
          "18-19",
          "19-20",
        ];
        boneNames.forEach((name) => {
          const bone = model.getObjectByName(name);
          if (bone) {
            handBones[name] = bone;
          } else {
            console.warn(`Bone "${name}" not found in model.`);
          }
        });

        console.log("Ossos carregados:", handBones);
      },
      undefined,
      (error) => {
        console.error("Erro ao carregar modelo:", error);
      },
    );

    camera.position.set(0, 1, 5);
    camera.lookAt(0, 0, 0);

    const animate = () => {
      requestAnimationFrame(animate);
      renderer.render(scene, camera);
    };

    animate();

    const socket = new WebSocket("ws://localhost:8765");

    socket.onopen = () => {
      console.log("Conexão WebSocket estabelecida.");
    };

    socket.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);

        console.log("data", data);

        Object.keys(data).forEach((boneName) => {
          const bone = handBones[boneName];
          if (bone) {
            const head = data[boneName].head;
            const tail = data[boneName].tail;

            const dx = tail.x - head.x;
            const dy = tail.y - head.y;
            const dz = tail.z - head.z;

            const magnitude = Math.sqrt(dx * dx + dy * dy + dz * dz);
            if (magnitude === 0) return;

            const normalizedDx = dx / magnitude;
            const normalizedDy = dy / magnitude;
            const normalizedDz = dz / magnitude;

            const angleX = Math.atan2(normalizedDy, normalizedDz);
            const angleY = Math.atan2(normalizedDx, normalizedDz);
            
            const maxAngle = Math.PI / 4; 
            const minAngle = -Math.PI / 4;

            const limitedAngleX = Math.max(
              minAngle,
              Math.min(maxAngle, angleX),
            );
            const limitedAngleY = Math.max(
              minAngle,
              Math.min(maxAngle, angleY),
            );

            bone.rotation.set(0, 0, 0);

            bone.position.x = limitedAngleX;
            bone.position.y = limitedAngleY;

            bone.updateMatrixWorld(true);
          }
          console.log("bone", bone);
        });
      } catch (error) {
        console.error("Erro ao processar dados WebSocket:", error);
      }
    };

    socket.onerror = (error) => {
      console.error("Erro no WebSocket:", error);
    };

    socket.onclose = () => {
      console.log("Conexão WebSocket fechada.");
    };

    return () => {
      mountRef.current.removeChild(renderer.domElement);
      renderer.dispose();
      socket.close();
    };
  }, []);

  return <div ref={mountRef} style={{ background: "transparent" }}></div>;
}

export default ThreeScene;
