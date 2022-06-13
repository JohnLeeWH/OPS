import "./App.css";
import React from "react";
import Test from "./components/Great";
import Welcome from "./components/Welcome";
import Hello from "./components/hello";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <Test name="123" nickName="一" >tttt</Test>
        <Test name="234" nickName="二" />
        <Test name="345" nickName="三" />
        <Welcome name="123" nickName="一" >www</Welcome>
      </div>
    )
  }
}

export default App;