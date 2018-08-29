import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './index.css';

class Header extends Component {
    constructor(props) {
        super(props);
        this.state = {
            "username" : [],
            "password" : [],
        }
    }

    handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    }

    handleClick = (e) => {
        let promise = axios.post("http://localhost:8000/token-auth/", this.state);

        promise
            .then(response => {
                localStorage.setItem("token", response.data.token);
                this.props.history.push(`/${this.state.username}/music`);
            })
            .catch(err => {
                console.error(err);
            });

    }

    render() {
        console.log("this.state", this.state);
        return (
            <div className="main-container">
                <div className="login">
                    <header className="header">
                        <h1 className="title">Welcome to Your Sheet Music Database</h1>
                    </header>
                    <div className="username-wrapper">
                        <div className="user-id">Username:</div>
                        <input className="input" onChange={this.handleChange} type="text" name="username" value={this.state.username}/>
                    </div>
                    <div className="password-wrapper">
                        <div className="password">Password:</div>
                        <input className="input" onChange={this.handleChange} type="password" name="password" value={this.state.password}/>
                    </div> 
                    <div className="submit-div">
                        <div className="submit-button" onClick={this.handleClick}>
                            <Link to="/badrequest" className="link-submit">Submit</Link>
                        </div>
                    </div>
                    <div className="account-sign-up">
                        <Link to="/register">Don't have an account? Sign up here!!</Link>
                    </div>
                </div>
            </div>
        );
    }
    }
    export default Header