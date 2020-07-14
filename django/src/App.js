import React, { Component } from 'react';
import logo from './logo.svg';
import { Route, Link } from 'react-router-dom';
import './App.css';
import Login from './components/Login';
import Notes from './components/Notes';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>

        <Link className='links' to='/notes'>Notes</Link>
        <Link className='links' to='/login'>Log In</Link>

        <Route path='/notes' component={Notes} />
        <Route path='/login' component={Login} />

      </div>
    );
  }
}

export default App;
