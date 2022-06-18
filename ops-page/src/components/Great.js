import React from "react";

//function Great() {
//    return <h1>Hello 2</h1>;
//}

const Great = (props) => {
    //console.log(props);
    const { name, nickName } = props;
    return (
        <div>
            <h1>Hello {name} aka {nickName}</h1>
        </div>);
};

export default Great;