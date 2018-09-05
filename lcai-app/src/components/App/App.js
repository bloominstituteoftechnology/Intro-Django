import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import logo from '../../logo.svg';

/**
 * IMPORT OCMPONENTS: App component is the Head of all others components.
 */
// import Component_1 from '../SideBar_/SideBar_';
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
            {/* <Component_1 />
            <Route component={Component_2} /> */}
          </div>
        </div>
      </div>
    );
  }
}

export default App;
