import React from 'react';

const Note = props => {
    return (
        <div className='note-container'>
            <p><strong>{props.note.title}</strong></p>
            <p>{props.note.content}</p>
        </div >
    );
}

export default Note;