import React, { Component } from 'react';
import axios from 'axios';

const API_DATA = process.env.REACT_APP_API_PROJECTS;

class Projects extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: '',
    };
  }
  render() {
    return (
      <div>
        <h1>HOME PAGE DATA</h1>
        <h3>This is the data served from the API</h3>

        <p>{JSON.stringify(this.state.data)}</p>
      </div>
    );
  }

  componentDidMount() {
    axios
      .get(API_DATA)
      .then(response => {
        console.log('API_DATA response', response.data);
        this.setState({ data: response.data });
      })
      .catch(e => {
        console.log('error', e);
      });
  }
}

export default Projects;
