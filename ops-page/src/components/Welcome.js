import React, { Component } from "react";

class Welcome extends Component {
    render() {
        return <h1>Welcome {this.props.name} aka {this.props.nickName} and {this.props.children}</h1>;
    }
}

export default Welcome;