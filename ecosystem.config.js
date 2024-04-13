module.exports = {
    apps : [{
      name: "api",
      script: "uvicorn",
      interpreter: "python3",
      args: "main:app --host 0.0.0.0 --port 8000 --reload"
    }]
  };
  