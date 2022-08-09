function connectDatabase() { // SO
  const didConnect = database.connect(); // SO
  if (didConnect) {
    return true;
  } else {
    console.log('Could not connect to database!'); // SO
    return false;
  }
}

function determineSupportAgent(ticket) { // NSO
  if (ticket.requestType === 'unknown') {
    return findStandardAgent(); // NSO
  }
  return findAgentByRequestType(ticket.requestType); // NSO
}

function isValid(email, password) { // NSO
  if (!email.includes('@') || password.length < 7) {
    console.log('Invalid input!'); // SO
    return false;
  }
  return true;
}
