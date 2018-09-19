import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      notes: []
    }
  }

  getNotes = () => {
    axios.get('http://127.0.0.1:8000/api/notes/', {
    headers: {
      "Authorization": "Token 246524d3f9d0ad7560a2b8423f858ae4e15dfb0f"
    }
    }).then(response => {
      console.log(response.data)
      this.setState({notes: response.data})
    }).catch(error => {
      console.log("YOU ERR", error)
    })
  }

  componentDidMount() {
    let data = {
      "username":"alec_jordan",
      "password":"suckas want beef"
    }
    axios.post('http://127.0.0.1:8000/api-token-auth/', data, {
    headers: {
      "Content-Type":"application/json"
    }
    }).then(response => {
      console.log(response.data)
    }).catch(error => {
      console.log("YOU ERR", error)
    })
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
        <div>
          {this.state.notes.map((note, index) => {
            return (<h2 key={index}>title: {note.title} content: {note.content}</h2>)
          })}
        </div>
      </div>
    );
  }
}

export default App;
