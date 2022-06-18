import React from "react";

function FunctionClick() {
    function clickHandler() {
        console.log("click!")
    }
    return (
        <div>
            <button onClick={clickHandler}>click</button>
        </div>
    )
}

export default FunctionClick;