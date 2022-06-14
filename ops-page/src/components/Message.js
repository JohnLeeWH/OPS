import React, { Component } from "react";

class Message extends Component {
    constructor() {
        super();
        this.state = {
            message: "欢迎！",
        };
    }
    changeMessage() {
        this.setState({ message: "click!" });
    }
    render() {
        return (
            <div>
                <h1>{this.state.message}</h1>
                <button onClick={() => this.changeMessage()}>subscribe</button>
            </div >
        );
    };
};

export default Message;