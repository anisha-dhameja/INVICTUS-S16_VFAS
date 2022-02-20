from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required
def feedback_form(request, slug, number_of_questions=1):
    if request.method == "POST":
        if "add_question" in request.POST:
            number_of_questions = request.POST['number_of_questions'] + 1
    print(request.POST.get("number_of_questions"))
    return render(
        request,
        "feedbacks/feedback_form.html",
        context={"number_of_questions": range(1, number_of_questions + 1), "slug": slug},
    )
