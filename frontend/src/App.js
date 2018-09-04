import React, { Component } from 'react';
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "XCSRF-Token";


class App extends Component {
  state = {
    user: {
      username: '',
      password: ''
    },
    token: '',
    notes: [{}]
  }

  handle_input = (e) => {
    let temp = JSON.parse(JSON.stringify(this.state.user))
    temp[e.target.name] = e.target.value
    this.setState({ user: temp })
  }

  handle_sign_in = (e) => {
    let user = this.state.user;
    axios.post('http://localhost:8000/api-token-auth/', user)
      .then(response => {
        let header = {
          Authorization: 'Token ' + response.data.token
        }
        let properties = 'id title content url'
        axios.get(`http://localhost:8000/graphql/?query={notes{${properties}}}`, header)
          .then(notes_res => {
            console.log(notes_res)
            let my_notes = Array.from(notes_res.data.data.notes)
            this.setState({ notes: my_notes })
          })
          .catch(notes_err => {
            console.log(notes_err)
          })
      })
      .catch(err => {
        console.log(err);
      })
  }

  render() {
    // console.log(this.state)
    return (
      <div className="App">
        <div>
          <input
            type='text'
            name='username'
            placeholder='username'
            onChange={this.handle_input}
          />
        </div>
        <div>
          <input
            type='password'
            name='password'
            placeholder='password'
            onChange={this.handle_input} />
        </div>
        <div>
          <button onClick={this.handle_sign_in}>Sign In</button>
        </div>
        <div>
          {this.state.notes.map((note, i) => {
            return (
              <div key={note.title + i}>
                <h3>Title: {note.title}</h3>
                <p>Contents: {note.content}</p>
                <p>URL: {note.url}</p>
                <p>Author: {this.state.user.username}</p>
              </div>
            )
          })}
        </div>
      </div>
    );
  }
}

export default App;
