import React, { Component } from "react";

class Welcome extends Component {
    render() {
        const { name, nickName } = this.props;
        return <h1>Welcome {name} aka {nickName} and {this.props.children}</h1>;
    }
}

export default Welcome;