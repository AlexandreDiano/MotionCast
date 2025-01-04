import cv2
import mediapipe as mp
import time
import asyncio
import websockets
import json  # Para enviar dados no formato JSON

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = float(detectionCon)
        self.trackCon = float(trackCon)

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNumber=0, draw=True):
        if not hasattr(self, "results") or not self.results.multi_hand_landmarks:
            return []

        lmList = []
        myHand = self.results.multi_hand_landmarks[handNumber]
        for id, lm in enumerate(myHand.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append({"id": id, "x": cx, "y": cy})
        return lmList

async def hand_tracking_server(websocket):
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture image")
            continue

        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        if len(lmList) != 0:
            # Simulação de dados: cada bone recebe um head e tail
            bone_data = {
                "0-1": {
                    "head": {"x": lmList[1]["x"], "y": lmList[1]["y"], "z": 0},
                    "tail": {"x": lmList[0]["x"], "y": lmList[0]["y"], "z": 0},
                },
                "1-2": {
                    "head": {"x": lmList[2]["x"], "y": lmList[2]["y"], "z": 0},
                    "tail": {"x": lmList[1]["x"], "y": lmList[1]["y"], "z": 0},
                },
                "2-3": {
                    "head": {"x": lmList[3]["x"], "y": lmList[3]["y"], "z": 0},
                    "tail": {"x": lmList[2]["x"], "y": lmList[2]["y"], "z": 0},
                },
                "3-4": {
                    "head": {"x": lmList[4]["x"], "y": lmList[4]["y"], "z": 0},
                    "tail": {"x": lmList[3]["x"], "y": lmList[3]["y"], "z": 0},
                },
                "0-5": {
                    "head": {"x": lmList[5]["x"], "y": lmList[5]["y"], "z": 0},
                    "tail": {"x": lmList[0]["x"], "y": lmList[0]["y"], "z": 0},
                },
                "5-6": {
                    "head": {"x": lmList[6]["x"], "y": lmList[6]["y"], "z": 0},
                    "tail": {"x": lmList[5]["x"], "y": lmList[5]["y"], "z": 0},
                },
                "6-7": {
                    "head": {"x": lmList[7]["x"], "y": lmList[7]["y"], "z": 0},
                    "tail": {"x": lmList[6]["x"], "y": lmList[6]["y"], "z": 0},
                },
                "7-8": {
                    "head": {"x": lmList[8]["x"], "y": lmList[8]["y"], "z": 0},
                    "tail": {"x": lmList[7]["x"], "y": lmList[7]["y"], "z": 0},
                },
                "5-9": {
                    "head": {"x": lmList[9]["x"], "y": lmList[9]["y"], "z": 0},
                    "tail": {"x": lmList[5]["x"], "y": lmList[5]["y"], "z": 0},
                },
                "9-10": {
                    "head": {"x": lmList[10]["x"], "y": lmList[10]["y"], "z": 0},
                    "tail": {"x": lmList[9]["x"], "y": lmList[9]["y"], "z": 0},
                },
                "10-11": {
                    "head": {"x": lmList[11]["x"], "y": lmList[11]["y"], "z": 0},
                    "tail": {"x": lmList[10]["x"], "y": lmList[10]["y"], "z": 0},
                },
                "11-12": {
                    "head": {"x": lmList[12]["x"], "y": lmList[12]["y"], "z": 0},
                    "tail": {"x": lmList[11]["x"], "y": lmList[11]["y"], "z": 0},
                },
                "0-17": {
                    "head": {"x": lmList[17]["x"], "y": lmList[17]["y"], "z": 0},
                    "tail": {"x": lmList[0]["x"], "y": lmList[0]["y"], "z": 0},
                },
                "17-13": {
                    "head": {"x": lmList[13]["x"], "y": lmList[13]["y"], "z": 0},
                    "tail": {"x": lmList[17]["x"], "y": lmList[17]["y"], "z": 0},
                },
                "13-14": {
                    "head": {"x": lmList[14]["x"], "y": lmList[14]["y"], "z": 0},
                    "tail": {"x": lmList[13]["x"], "y": lmList[13]["y"], "z": 0},
                },
                "14-15": {
                    "head": {"x": lmList[15]["x"], "y": lmList[15]["y"], "z": 0},
                    "tail": {"x": lmList[14]["x"], "y": lmList[14]["y"], "z": 0},
                },
                "15-16": {
                    "head": {"x": lmList[16]["x"], "y": lmList[16]["y"], "z": 0},
                    "tail": {"x": lmList[15]["x"], "y": lmList[15]["y"], "z": 0},
                },
                "17-18": {
                    "head": {"x": lmList[18]["x"], "y": lmList[18]["y"], "z": 0},
                    "tail": {"x": lmList[17]["x"], "y": lmList[17]["y"], "z": 0},
                },
                "18-19": {
                    "head": {"x": lmList[19]["x"], "y": lmList[19]["y"], "z": 0},
                    "tail": {"x": lmList[18]["x"], "y": lmList[18]["y"], "z": 0},
                },
                "19-20": {
                    "head": {"x": lmList[20]["x"], "y": lmList[20]["y"], "z": 0},
                    "tail": {"x": lmList[19]["x"], "y": lmList[19]["y"], "z": 0},
                },
            }
            await websocket.send(json.dumps(bone_data))

        # Exibir vídeo
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()



async def main():
    async with websockets.serve(hand_tracking_server, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Mantém o servidor ativo

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Usa asyncio.run para gerenciar o loop de eventos
    except KeyboardInterrupt:
        print("Server stopped.")
