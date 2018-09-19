import React from 'react';
import '../App.css';
import axios from 'axios';
import Login from './Login';

const Authenticate = ProtectedComponent => 
    class InnerApp extends React.Component {
        constructor(props) {
            super(props);
            this.state = {
                loggedIn: false
            }
        }

        componentDidMount() {
            if (localStorage.getItem('token')) this.setState({
                loggedIn: true
            });
        }

        render() {
            return (this.state.loggedIn ? <ProtectedComponent />: <Login />);
        }
    }


export default Authenticate