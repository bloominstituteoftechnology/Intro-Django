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
        <div className="projects">
        {this.state.projects.map(p => <div className="project"><p>Language: {p.language}</p><p>Concepts: {p.concept}</p></div>)}
        </div>
      </div>
    );
  }
}

export default App;
