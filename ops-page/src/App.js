import "./App.css";
import React from "react";
import Test from "./components/Great";
import Welcome from "./components/Welcome";
import Hello from "./components/hello";
import Message from "./components/Message";
import Counter from "./components/Counter";
import Great from "./components/Great";
import FunctionClick from "./components/FunctionClick";
import ClassClick from "./components/ClassClick";
import EventBind from "./components/EventBind";
import ParentComponent from "./components/parentComponent";
import UserGreeting from "./components/UserGreeting";
import NameList from "./components/NameList";

class App extends React.Component {

  render() {
    return (
      <div className="App">
        <NameList />
      </div>
    )
  }
}

export default App;