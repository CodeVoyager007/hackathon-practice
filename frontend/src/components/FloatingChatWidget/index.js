import React, { useState, useEffect } from 'react';
import Chatbot from '@site/src/components/Chatbot';
import styles from './styles.module.css';

const FloatingChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isClient, setIsClient] = useState(false);
  const [selection, setSelection] = useState(null);
  const [tooltipPosition, setTooltipPosition] = useState({ top: 0, left: 0 });

  useEffect(() => {
    setIsClient(true);
  }, []);

  const handleMouseUp = () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText) {
        const range = window.getSelection().getRangeAt(0);
        const rect = range.getBoundingClientRect();
        setSelection(selectedText);
        setTooltipPosition({
            top: rect.bottom + window.scrollY + 5,
            left: rect.left + window.scrollX + rect.width / 2,
        });
    } else {
      setSelection(null);
    }
  };

  const handleAsk = () => {
    setIsOpen(true);
  };

  const handleCopy = () => {
    if (selection) {
      navigator.clipboard.writeText(selection);
    }
    setSelection(null);
  };
  
  useEffect(() => {
    document.addEventListener('mouseup', handleMouseUp);
    const handleScroll = () => setSelection(null);
    document.addEventListener('scroll', handleScroll);
    return () => {
      document.removeEventListener('mouseup', handleMouseUp);
      document.removeEventListener('scroll', handleScroll);
    };
  }, []);

  const toggleChatWindow = () => {
    setIsOpen(!isOpen);
    setSelection(null);
  };

  if (!isClient) {
    return null;
  }

  return (
    <div className={styles.widgetContainer}>
        {selection && !isOpen && (
            <div
            className={styles.tooltip}
            style={{ top: tooltipPosition.top, left: tooltipPosition.left }}
            >
                <button onClick={handleCopy}>Copy</button>
                <button onClick={handleAsk}>Ask</button>
            </div>
        )}
      <div className={styles.launcherButton} onClick={toggleChatWindow}>
        <span>{isOpen ? '✕' : '💬'}</span>
      </div>
      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <h2>AI Assistant</h2>
          </div>
          <Chatbot selection={selection} />
        </div>
      )}
    </div>
  );
};

export default FloatingChatWidget;