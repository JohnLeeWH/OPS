import "./App.css";
import React from "react";
import Test from "./components/Great";
import Welcome from "./components/Welcome";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <Test />
        <Welcome />
      </div>
    )
  }
}

export default App;