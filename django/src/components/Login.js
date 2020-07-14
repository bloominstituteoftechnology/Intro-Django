import React from 'react';
import axios from 'axios';

class Login extends React.Component {
    constructor() {
        super();

        this.state = {
            username: '',
            password: ''
        }
    }

    handleInput = event => {
        this.setState({ [event.target.name]: event.target.value })
    }

    logIn = () => {
        const user = { username: this.state.username, password: this.state.password };

        axios
            .post('http://localhost:8000/api-token-auth/', user)
            .then(response => {
                localStorage.setItem('token', 'token ' + response.data.token);
                this.props.history.push('/notes');
            })
            .catch(err => console.log(err));
    }

    render() {
        return (
            <form onSubmit={event => event.preventDefault()}>
                <input onChange={this.handleInput} placeholder='Username' type='text' name='username' />
                <input onChange={this.handleInput} placeholder='Password' type='password' name='password' />
                <button onClick={this.logIn}>Log In</button>
            </form>
        );
    }
}

export default Login;
