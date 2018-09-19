import React, {Component} from 'react';
import '../../App.css';
import axios from 'axios';

const Authenticate = ProtectedComponent => {
    class InnerApp extends React.Component {
        constructor(props) {
            super(props)
            this.state = {
                loggedIn = false
            }
        }

        componentDidMount() {
            if localStorage.getItem('token') this.setState({
                loggedIn: true
            });
        }
    }
}
