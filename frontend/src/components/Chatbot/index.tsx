import React, { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import styles from './styles.module.css';

const suggestedPrompts = [
  "What is the main theme of the book?",
  "Who is the main character?",
  "Summarize the first chapter.",
  "What is the author's background?"
];

const Chatbot = ({ selection }) => {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatHistoryRef = useRef(null);

  useEffect(() => {
    // Scroll to the bottom of the chat history when messages change
    if (chatHistoryRef.current) {
      chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
    }
  }, [messages, loading]);

  useEffect(() => {
    if (selection) {
      setQuery(selection);
    }
  }, [selection]);


  const handleQueryChange = (event) => {
    setQuery(event.target.value);
  };

  const sendQueryToBackend = async (currentQuery, context = null) => {
    setLoading(true);
    let messageHistory = [...messages, { sender: 'user', text: currentQuery }];
    setMessages(messageHistory);
    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: currentQuery, context: context }),
      });

      if (response.ok) {
        const data = await response.json();
        setMessages([...messageHistory, { sender: 'bot', text: data.answer }]);
      } else {
        setMessages([...messageHistory, { sender: 'bot', text: 'Error: Could not get a response.' }]);
      }
    } catch (error) {
      setMessages([...messageHistory, { sender: 'bot', text: 'Error: Could not connect to the chatbot service.' }]);
    } finally {
      setLoading(false);
      setQuery('');
    }
  }

  const handleSendMessage = () => {
    if (!query.trim()) return;
    sendQueryToBackend(query);
  };

  const handleSuggestedPromptClick = (prompt) => {
    sendQueryToBackend(prompt);
  };

  return (
    <div className={styles.chatbotContainer}>
      <div className={styles.chatHistory} ref={chatHistoryRef}>
        {messages.length === 0 && !loading && (
          <div className={styles.suggestedPrompts}>
            <h4>Suggested Prompts</h4>
            {suggestedPrompts.map((prompt, index) => (
              <button key={index} onClick={() => handleSuggestedPromptClick(prompt)} className={styles.suggestedPromptButton}>
                {prompt}
              </button>
            ))}
          </div>
        )}
        {messages.map((message, index) => (
          <div key={index} className={`${styles.message} ${styles[message.sender]}`}>
            {message.sender === 'bot' ? (
              <ReactMarkdown>{message.text}</ReactMarkdown>
            ) : (
              <p>{message.text}</p>
            )}
          </div>
        ))}
        {loading && <div className={`${styles.message} ${styles.bot}`}><p>Thinking...</p></div>}
      </div>
      <div className={styles.chatInput}>
        <textarea
          value={query}
          onChange={handleQueryChange}
          onKeyPress={(e) => e.key === 'Enter' && !e.shiftKey && handleSendMessage()}
          placeholder="Ask something..."
          disabled={loading}
          rows={3}
        />
        <button onClick={handleSendMessage} disabled={loading}>
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;