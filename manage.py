from flask import Flask, jsonify, render_template, request, redirect, session, g
from Sflask import create_app

from redis import Redis
from flask_session import RedisSessionInterface

app = create_app()


if __name__ == '__main__':
    app.run()