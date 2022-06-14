import "./App.css";
import React from "react";
import Test from "./components/Great";
import Welcome from "./components/Welcome";
import Hello from "./components/hello";
import Message from "./components/Message";
import Counter from "./components/Counter";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <Message />
        <Counter />
      </div>
    )
  }
}

export default App;