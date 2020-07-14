import React from 'react';
import axios from 'axios';
import Note from './Note';

class Notes extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            notes: []
        }
    }

    componentDidMount() {
        const token = localStorage.getItem('token');

        if (token) {
            axios
                .get('http://localhost:8000/api/notes/', { headers: { Authorization: token } })
                .then(response => this.setState({ notes: response.data }))
                .catch(err => console.log(err));
        } else {
            this.props.history.push('/login');
        }
    }

    logout = () => {
        localStorage.removeItem('token');
        window.location.reload();
    }

    render() {
        return (
            <div>
                <button onClick={this.logout}>Logout</button>
                {this.state.notes.map(note => <Note key={Math.random()} note={note} />)}
            </div>
        );
    }
}

export default Notes;