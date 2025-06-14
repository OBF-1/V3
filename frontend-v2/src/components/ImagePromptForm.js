import React, { useState } from 'react';
function ImagePromptForm() {
  const [prompt, setPrompt] = useState('');
  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/generate-image', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    const data = await res.json();
    console.log(data);
  };
  return (
    <form onSubmit={handleSubmit}>
      <input value={prompt} onChange={e => setPrompt(e.target.value)} placeholder='Enter prompt' />
      <button type='submit'>Generate</button>
    </form>
  );
}
export default ImagePromptForm;
