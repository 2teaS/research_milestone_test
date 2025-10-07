from django.shortcuts import render
from django.db.models import Count
from .models import Record
from .forms import FilterForm

def home(request):
    form = FilterForm(request.GET or None)

    # start UNSLICED, apply filters
    qs = Record.objects.all()

    if form.is_valid():
        src_ip = form.cleaned_data.get("src_ip")
        dst_ip = form.cleaned_data.get("dst_ip")
        proto = form.cleaned_data.get("proto")
        min_port = form.cleaned_data.get("min_port")
        max_port = form.cleaned_data.get("max_port")

        if src_ip:
            qs = qs.filter(src_ip__icontains=src_ip)
        if dst_ip:
            qs = qs.filter(dst_ip__icontains=dst_ip)
        if proto:
            qs = qs.filter(proto__iexact=proto)
        if min_port is not None:
            qs = qs.filter(dst_port__gte=min_port)
        if max_port is not None:
            qs = qs.filter(dst_port__lte=max_port)

    # CHART: build from the filtered, unsliced queryset
    top_ports = (
        qs.values("dst_port")
          .annotate(cnt=Count("id"))
          .order_by("-cnt")[:15]
    )
    chart_labels = [str(x["dst_port"]) for x in top_ports if x["dst_port"] is not None]
    chart_values = [x["cnt"] for x in top_ports if x["dst_port"] is not None]

    # TABLE: slice only here for display
    records = qs.order_by("-timestamp")[:200]
    count = qs.count()

    return render(request, "network/home.html", {
        "form": form,
        "records": records,
        "count": count,
        "chart_labels": chart_labels,
        "chart_values": chart_values,
    })
