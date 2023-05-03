import React, { useState } from 'react';

function VotingSystem({ ideas, maxVotes, onVote }) {
  const [votes, setVotes] = useState([]);

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
          {ideas.map((idea) => (
            <li key={idea.id} className="list-group-item">
              <button
                className="btn btn-primary"
                disabled={votes.length >= maxVotes || votes.includes(idea.id)}
                onClick={() => handleVote(idea.id)}
              >
                {idea.name}
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default VotingSystem;
