import React, { useState } from 'react';

const API_BASE = "http://127.0.0.1:8000/api/accounts";

export default function App() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [accountType, setAccountType] = useState('SAVINGS');
  
  const [accountId, setAccountId] = useState('');
  const [account, setAccount] = useState(null);
  const [amount, setAmount] = useState('');
  const [transactions, setTransactions] = useState([]);

  const handleCreate = async (e) => {
    e.preventDefault();
    const res = await fetch(API_BASE, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, accountType })
    });
    const data = await res.json();
    alert(`Account Created! ID: ${data.accountId}`);
    setAccountId(data.accountId);
    setAccount(data);
  };

  const handleFetchAccount = async () => {
    const res = await fetch(`${API_BASE}/${accountId}`);
    if (res.ok) {
      const data = await res.json();
      setAccount(data);
    } else {
      alert("Account not found");
    }
  };

  const handleTransact = async (type) => {
    const res = await fetch(`${API_BASE}/${accountId}/${type}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: parseFloat(amount) })
    });
    if (res.ok) {
      handleFetchAccount();
      setAmount('');
    } else {
      const err = await res.json();
      alert(err.detail);
    }
  };

  const handleFetchTransactions = async () => {
    const res = await fetch(`${API_BASE}/${accountId}/transactions`);
    const data = await res.json();
    setTransactions(data);
  };

  return (
    <div style={{ padding: 20, fontFamily: 'sans-serif', maxWidth: 500 }}>
      <h2>Simple Bank App</h2>

      {/* Create Account Form */}
      <form onSubmit={handleCreate} style={{ border: '1px solid #ccc', padding: 15, marginBottom: 15 }}>
        <h3>Create Account</h3>
        <input placeholder="Name" value={name} onChange={e => setName(e.target.value)} required /><br/><br/>
        <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required /><br/><br/>
        <select value={accountType} onChange={e => setAccountType(e.target.value)}>
          <option value="SAVINGS">SAVINGS</option>
          <option value="CHECKING">CHECKING</option>
        </select><br/><br/>
        <button type="submit">Create</button>
      </form>

      {/* Account Operations */}
      <div style={{ border: '1px solid #ccc', padding: 15 }}>
        <h3>Find & Manage Account</h3>
        <input placeholder="Account ID" value={accountId} onChange={e => setAccountId(e.target.value)} />
        <button onClick={handleFetchAccount}>Search</button>

        {account && (
          <div style={{ marginTop: 15 }}>
            <p><strong>Name:</strong> {account.userName}</p>
            <p><strong>Balance:</strong> ${account.balance}</p>

            <input placeholder="Amount" type="number" value={amount} onChange={e => setAmount(e.target.value)} /><br/><br/>
            <button onClick={() => handleTransact('deposit')}>Deposit</button>
            <button onClick={() => handleTransact('withdraw')} style={{ marginLeft: 10 }}>Withdraw</button>
            <button onClick={handleFetchTransactions} style={{ marginLeft: 10 }}>History</button>
          </div>
        )}
      </div>

      {/* Transactions Table */}
      {transactions.length > 0 && (
        <div style={{ marginTop: 15 }}>
          <h3>History</h3>
          <table border="1" cellPadding="5" style={{ width: '100%' }}>
            <thead>
              <tr><th>Type</th><th>Amount</th><th>Date</th></tr>
            </thead>
            <tbody>
              {transactions.map((t, idx) => (
                <tr key={idx}><td>{t.type}</td><td>${t.amount}</td><td>{t.date}</td></tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}