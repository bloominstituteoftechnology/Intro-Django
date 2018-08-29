import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import "../index.css";
import axios from 'axios';
import house from '../house.png'

class NotesList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            notes: [],
        }
    }

    componentDidMount() {
        let promise = axios.get(`http://localhost:8000/api/notes`);
        promise.then((response) => {
            const notes = response.data
            console.log("CDM notes", notes);
            this.setState({
                notes: notes
            });
            })
            .catch((error) => {
                console.error(error);
            })
    }
    render() {
        console.log(this.state.notes);
        return (
            <div>
                <div className="home-link"><Link to="/"><img className="house-pic"src={house} alt="home"/></Link></div>
                <div className="main-note-container">
                    {this.state.notes.map(note => {
                        return (
                            <div key={note.id} className="note-indiv">
                                <h1>{note.title}</h1>   
                                <p>{note.content}</p>
                            </div>              )
                    })}
                </div>
                <div><Link to="/create"><h4 className="create-link">2 + 2 = 5</h4></Link></div>
            </div>
        );
    }
}

export default NotesList;