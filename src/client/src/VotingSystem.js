import React, { useState, useEffect } from 'react';

function VotingSystem({ ideas, maxVotes, onVote, numMembers }) {
  const [votes, setVotes] = useState([]);
  const [responseMessage, setResponseMessage] = useState('');

  useEffect(() => {
    if (votes.length === maxVotes) {
      console.log("votes: " + votes);
      fetch('/vote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ votes, numMembers }),
      })
        .then(response => response.json())
        .then(data => {
          // handle response data
          setResponseMessage(data.message);
          console.log(responseMessage)
        })
        .catch(error => {
          // handle error
        });
    }
  }, [votes, maxVotes, numMembers]);

  const handleVote = (ideaId) => {
    if (votes.length < maxVotes && !votes.includes(ideaId)) {
      setVotes([...votes, ideaId]);
      onVote([...votes, ideaId]);
    }
  };

  return (
    <div className="card">
      <div className="card-header bg-secondary text-white">
        <h2>Vote for your favorite ideas ({maxVotes} votes)</h2>
      </div>
      <div className="card-body">
        <ul className="list-group">
          {ideas.length > 0 &&
            ideas.map((idea) => (
              <li key={idea.id} className="list-group-item">
                <button
                  className="btn btn-primary"
                  disabled={votes.length >= maxVotes || votes.includes(idea.id)}
                  onClick={() => handleVote(idea.id)}
                >
                  {idea.name}
                </button>
                <p>{idea.description}</p>
              </li>
            ))}
        </ul>
        {responseMessage && (
          <div className="response-message">
            <h3>{responseMessage}</h3>
          </div>
        )}
      </div>
    </div>
  );
}

export default VotingSystem;
