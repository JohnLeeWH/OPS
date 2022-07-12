import React, { Component } from "react";

class Form extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            comment: "",
            topic: '1',
        }
    };
    handleUsernameChange = event => {
        this.setState({ username: event.target.value });
        // console.log(this.state.username);
    };
    handleCommentChange = event => {
        this.setState({ comment: event.target.value });
        // console.log(this.state.username);
    };
    handleTopicChange = event => {
        this.setState({ topic: event.target.value });
        // console.log(this.state.username);
    };
    handleSubmit = event => {
        alert(`${this.state.username} ${this.state.comment} ${this.state.topic}`);
        event.preventDefault();//submit 不刷新
    }
    render() {
        const { username, comment, topic } = this.state;
        return (

            <form onSubmit={this.handleSubmit}>
                <div>
                    <label>用户名：</label>
                    <input value={username} onChange={this.handleUsernameChange}></input>
                </div>
                <div>
                    <label>评论：</label>
                    <textarea value={comment} onChange={this.handleCommentChange}></textarea>
                </div>
                <div>
                    <label>主题：</label>
                    <select value={topic} onChange={this.handleTopicChange}>
                        <option value="1" >1</option>
                        <option value="22">22</option>
                        <option value="333">333</option>
                    </select>
                </div>
                <button type="submit">提交</button>
            </form>

        )
    }
}

export default Form;