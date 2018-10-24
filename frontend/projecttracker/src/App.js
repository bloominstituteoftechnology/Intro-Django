import React, { Component } from 'react';
import './App.css';
import axios from "axios"

class App extends Component {
  constructor() {
    super();
    this.state = {
      projects: []
  }
}

  componentDidMount() {
    this.getProjects()
  }

  getProjects = () => {
    axios
    .get("http://localhost:8000/api/projects/")
    .then(response => {
      this.setState({ projects: response.data })
      console.log(response.data)
    })
  }
  render() {
    return (
      <div className="App">
        <h1>Hellluuuu</h1>
        <div>
        {this.state.projects.map(p => <div>{p.language}</div>)}
        </div>
      </div>
    );
  }
}

export default App;
