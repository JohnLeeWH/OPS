import React from "react";
import "./myStyles.css";


function StyleSheet(props) {
    let className = props.primary ? "primary" : ""
    return (
        <h1 className={`${className} font-xl`}>样式单</h1>
    )


}

export default StyleSheet;