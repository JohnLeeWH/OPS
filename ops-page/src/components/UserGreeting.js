import React, { Component } from "react";
import Hello from "./hello";

class UserGreeting extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isLoggedIn: true,
        };
    }
    render() {
        return this.state.isLoggedIn && <div>hello user</div>;
        
        // return this.state.isLoggedIn ? (<div>Hello user</div>) : (<div>hello guest</div>)
        // let message;
        // if (this.state.isLoggedIn) {
        //     message = <div>hello user</div>
        // } else {
        //     message = <div>hello guest</div>
        // }
        // return <div>{message}</div>
        // if (this.state.isLoggedIn) {
        //     return <div>hello user</div>
        // } else {
        //     return <div>hello guest</div>
        // }
    }
}

export default UserGreeting;