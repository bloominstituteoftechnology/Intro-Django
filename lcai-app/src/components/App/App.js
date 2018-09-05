import logo from '../../logo.svg';
import React, { Component } from 'react';
import { Route, Link, Switch } from 'react-router-dom';
import axios from 'axios';

// COMPONENTS
import Home from '../Home/Home';

const API_AUTH = process.env.REACT_APP_API_AUTH_ENPOINT;
const AUTH_USERNAME = process.env.REACT_APP_AUTH_USERNAME;
const AUTH_PASSWORD = process.env.REACT_APP_AUTH_PASSWORD;

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      superduper: '',
    };
  }

  componentDidMount() {
    // Mock an Auth process by passing a hardcoded user and password
    console.log({ API_AUTH, AUTH_USERNAME, AUTH_PASSWORD });
    const auth = axios.post(API_AUTH, { username: AUTH_USERNAME, password: AUTH_PASSWORD });
    auth
      .then(response => {
        console.log('response', response);
        // TODO Add Token to 'state'
        const { token } = response.data;
        this.setState({ superduper: token });
      })
      .catch(e => {
        console.log('error', e);
      });
  }

  render() {
    const Page404 = (
      <div>
        <br />
        <h5>Something went wrong,</h5>
        <br />
        <p>the page you are looking for is no here...</p>
        <br />
        <Link to="/">
          <button>Go back to home.</button>
        </Link>
      </div>
    );

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <div className="container custom-container">
          <div className="row">
            <Switch>
              {/* ADD COMPONENTS HERE */}
              <Route exact path="/" component={Home} />
              <Route component={() => Page404} />
            </Switch>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
