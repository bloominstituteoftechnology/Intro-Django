import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import './index.css';
import Header from './Header';
import MusicList from './MusicList';
import FourOhFour from './FourOhFour';

class App extends Component {
  render() {
    return (
      <div className="router">
        <Switch>
          <Route exact path="/" component={Header}/>
          <Route path="/music" component={MusicList}/>
          <Route path = "/badrequest" component={FourOhFour}/>
        </Switch>
      </div>
    );
  }
}

export default App;
