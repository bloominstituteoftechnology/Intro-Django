import React, { Component } from 'react';
import { Route, Link, Switch } from 'react-router-dom';
import logo from '../../logo.svg';

/**
 * IMPORT OCMPONENTS: App component is the Head of all others components.
 */
import Home from '../Home/Home';
// import Component_2 from '../Main_/Main_';

class App extends Component {
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
