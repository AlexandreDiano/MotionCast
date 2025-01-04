import ThreeScene from "./components/ThreeScene.jsx";

function App() {
  return (
    <div className="wrapper flex-col">
      <h1 className="flex justify-center items-center">Motion Cast</h1>
      <div className="flex justify-center self-center bg-white w-9/12 h-[90vh] mt-3 rounded-lg">
        <ThreeScene />
      </div>
    </div>
  );
}

export default App;
