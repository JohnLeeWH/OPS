import "./App.css";
import React from "react";
import Test from "./components/Great";
import Welcome from "./components/Welcome";
import Hello from "./components/hello";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <Test />
        <Welcome />
        <Hello />
      </div>
    )
  }
}

export default App;