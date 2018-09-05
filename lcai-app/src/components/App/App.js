import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import logo from '../../logo.svg';

/**
 * IMPORT OCMPONENTS: App component is the Head of all others components.
 */
import Home from '../Home/Home';
// import Component_2 from '../Main_/Main_';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <div className="container custom-container">
          <div className="row">
            {/* ADD COMPONENTS HERE */}
            <Route exact path="/" component={Home} />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
