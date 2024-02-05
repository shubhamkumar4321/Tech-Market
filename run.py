from market import app

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     try:
#         app.run(debug=True)
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(130)
#         except SystemExit:
#             os._exit(130)