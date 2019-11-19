import React, { Component } from 'react';
import './App.css';
import axios from 'axios'

class App extends Component {

  state = {
    questions: []
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/questions/')
    .then((response)=>{
      this.setState({ questions: response.data })
      console.log(response);
    })
    .catch(error => {
      console.log(error);
    })
  }
  render() {
    const questions = this.state.questions.slice().reverse();
    return (
      <div className="smurf-list">
      {questions.map(question => {
        return (
         
            <div className="question-card">
              <h2>{ question.question_text }</h2>
            </div>
  
        );
      })}
    </div>
    );
  }
}

export default App;
