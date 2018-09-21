import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import Authenticate from './components/Authenticate';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      notes: []
    }
  }

  getNotes = () => {
    let token = 'Token ' + localStorage.getItem('token')
    axios.get('https://alec-lambda-django.herokuapp.com/api/notes/', {
    headers: {
      "Authorization": token
    }
    }).then(response => {
      console.log('THIS WORKED', response.data)
      this.setState({notes: response.data})
    }).catch(error => {
      console.log("YOU ERR", error)
    })
  }

  logOut = () => {
    localStorage.removeItem('token')
    window.location.reload()
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to PReact</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <button onClick={this.getNotes}>Get Notes</button>
        <button onClick={this.logOut}>Log Out</button>
        <div>
          {this.state.notes.map((note, index) => {
            return (<h2 key={index}>title: {note.title} content: {note.content}</h2>)
          })}
        </div>
      </div>
    );
  }
}

export default Authenticate(App);
